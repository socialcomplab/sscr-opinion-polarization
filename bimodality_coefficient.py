def bi_modality_coef_sample(skew, kurt, n):
    upper = skew**2 + 1
    lower_right = (3*((n-1)**2))/((n-2)*(n-3))
    return upper/(kurt + lower_right)