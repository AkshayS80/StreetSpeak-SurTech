from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportForm
from .models import Report, UserToken, Reward

from django.contrib.auth.forms import UserCreationForm, User

import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import os

# Load model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), "pothole_model.h5")
cnn_model = tf.keras.models.load_model(MODEL_PATH)


def home(request):
    recent_issues = Report.objects.order_by('-submitted_at')[:4]
    tokens = 0
    if request.user.is_authenticated:
        token_obj, _ = UserToken.objects.get_or_create(user=request.user)
        tokens = token_obj.tokens
    return render(request, 'home.html', {'tokens': tokens, 'recent_issues': recent_issues})

def report_issue(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            
            img_path = report.image.path  # the uploaded image path on server
            test_img = image.load_img(img_path, target_size=(64, 64))
            test_img = image.img_to_array(test_img)
            test_img = np.expand_dims(test_img, axis=0)

            result = cnn_model.predict(test_img)

            # If CNN sees pothole
            if result[0][0] > 0.5:
                report.scanned = True
                report.priority = 1   # pothole
            else:
                report.scanned = True
                report.priority = 0   # normal

            report.save()

            # Token reward (same)
            token_obj, _ = UserToken.objects.get_or_create(user=request.user)
            token_obj.tokens += 10
            token_obj.save()

            # ✅ FIX: pass report to thankyou.html
            return render(request, 'thankyou.html', {'report': report})
    else:
        form = ReportForm()

    # ✅ FIX: show the form again if GET or invalid POST
    return render(request, 'report.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserToken.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def token_history(request):
    reports = Report.objects.filter(user=request.user).order_by('-submitted_at')
    token_obj, _ = UserToken.objects.get_or_create(user=request.user)
    return render(request, 'token_history.html', {'reports': reports, 'tokens': token_obj.tokens})

def leaderboard(request):
    top_users = UserToken.objects.select_related('user').order_by('-tokens')[:10]
    return render(request, 'leaderboard.html', {'top_users': top_users})

def rewards_view(request):
    rewards = Reward.objects.all()
    token_obj, _ = UserToken.objects.get_or_create(user=request.user)
    return render(request, "rewards.html", {"rewards": rewards, "tokens": token_obj.tokens})

def claim_reward(request, reward_id):
    reward = get_object_or_404(Reward, id=reward_id)
    token_obj, _ = UserToken.objects.get_or_create(user=request.user)

    if token_obj.tokens >= reward.cost:
        token_obj.tokens -= reward.cost
        token_obj.save()
        # You can also log redemption here if needed
        return render(request, "thankyou_reward.html", {"reward": reward})
    else:
        return render(request, "not_enough_tokens.html", {"reward": reward})
