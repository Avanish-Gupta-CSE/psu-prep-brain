import os

user_dir = r'C:\Users\agupt1'
search_dirs = [
    os.path.join(user_dir, 'Downloads'),
    os.path.join(user_dir, 'Documents'),
    os.path.join(user_dir, 'Desktop'),
    os.path.join(user_dir, 'Projects')
]

exclude_dirs = {'node_modules', '.git', '.cursor', 'AppData', '$Recycle.Bin', 'venv', '.venv'}

matches = []
for sdir in search_dirs:
    if os.path.exists(sdir):
        for root, dirs, files in os.walk(sdir, topdown=True):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for f in files:
                lf = f.lower()
                if ('gate' in lf or 'score' in lf) and (lf.endswith('.pdf') or lf.endswith('.png') or lf.endswith('.jpg') or lf.endswith('.jpeg')):
                    fp = os.path.join(root, f)
                    matches.append((f, fp))

print(f"Found {len(matches)} matching files:")
for f, fp in matches:
    print(f"{f} -> {fp}")
