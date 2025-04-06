from setuptools import setup, find_packages

# Основные зависимости
INSTALL_REQUIRES = [
    "pyrogram>=2.0",
]

# Чтение зависимостей из requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requires = [line.strip() for line in f]

# Чтение содержимого README для long_description
with open("README.md", encoding="utf-8") as f:
    readme = f.read()

# Основная конфигурация setup
setup(
    name="monkeygram_patch",
    version="0.1",
    description="Monkey patch for Pyrogram to support long messages",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="deadboizxc",
    author_email="deadboi.zxc@gmail.com",
    url="https://github.com/deadboizxc/monkeygram_patch",  # Убедитесь, что у вас есть репозиторий по этому адресу
    download_url="https://github.com/deadboizxc/monkeygram_patch/releases/latest",  # Обновите по мере появления релизов
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="telegram, long messages, pyrogram, bot, async",
    project_urls={
        "Tracker": "https://github.com/deadboizxc/monkeygram_patch/issues",
        "Source": "https://github.com/deadboizxc/monkeygram_patch",
        "Documentation": "https://github.com/deadboizxc/monkeygram_patch/wiki",  # Если есть вики
    },
    python_requires=">=3.7",
    packages=find_packages(exclude=["tests*"]),
    package_data={
        "monkeygram_patch": ["py.typed"],  # Если используется типизация
    },
    zip_safe=False,
    install_requires=INSTALL_REQUIRES + requires,  # Учитываем зависимости из файла requirements.txt
    extras_require={  # Дополнительные зависимости (например, для тестирования)
        "dev": [
            "pytest",  # Для тестирования
            "tox",     # Для многоплатформенных тестов
        ],
        "docs": [
            "sphinx",             # Для генерации документации
            "sphinx-rtd-theme",   # Тема для Sphinx (используется на ReadTheDocs)
        ],
    },
)
