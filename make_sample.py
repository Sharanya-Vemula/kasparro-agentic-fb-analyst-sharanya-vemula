import pandas as pd

df = pd.read_csv("data/synthetic_fb_ads_undergarments.csv")
sample = df.sample(800, random_state=42)
sample.to_csv("data/sample_fb_ads.csv", index=False)

print("sample_fb_ads.csv created successfully!")
