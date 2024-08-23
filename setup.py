import setuptools

with open("README.md" ,  "r", encoding="utf-8") as f:
    lon_description = f.read()


__version__="0.0.0"

REPO_NAME="End-to-end-ML-project--Red-Wine"
AUTHOR_USER_NAME="ShreyasRede"
SRC_REPO="mlProject"
AUTHORE_EMAIL="shreyasrede0@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    author_email=AUTHORE_EMAIL,
    description="A samll pythone package for ml app"
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)