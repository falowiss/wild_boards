import os

project_root = "."

print("Структура проекта:")
print("-" * 50)

for root, dirs, files in os.walk(project_root):
    # Пропускаем служебные папки
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv', '.venv', '.idea']]
    
    level = root.replace(project_root, '').count(os.sep)
    indent = ' ' * 4 * level
    
    # Выводим папку
    if level == 0:
        print(f"{os.path.basename(root)}/")
    else:
        print(f"{indent}{os.path.basename(root)}/")
    
    # Выводим файлы Python
    subindent = ' ' * 4 * (level + 1)
    for file in sorted(files):
        if file.endswith('.py'):
            print(f"{subindent}{file}")

print("\nHTML шаблоны:")
print("-" * 50)
for root, dirs, files in os.walk(project_root):
    dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv', '.venv', '.idea']]
    for file in files:
        if file.endswith('.html'):
            print(f"{os.path.join(root, file)}")