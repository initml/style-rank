from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stylebench",
    version="0.1",
    author="Eyal Benaroche",
    author_email="eyal.benaroche@jasper.ai",
    description="Stylying unified benchmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gojasper/style-benchmark",
    project_urls={"Bug Tracker": "https://github.com/gojasper/style-benchmark/issues"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "black>=24.2.0",
        "controlnet-aux==0.0.7",
        "einops==0.7.0",
        "isort>=5.13.2",
        "lightning==2.2.5",
        "lpips==0.1.4",
        "opencv-python==4.9.0.80",
        "peft==0.9.0",
        "pillow-avif-plugin==1.4.6",
        "pydantic>=2.6.1",
        "scipy>=1.12.0",
        "sentencepiece>=0.2.0",
        "timm==0.9.16",
        "tokenizers>=0.15.2",
        "tqdm>=4.66.0",
        "transformers==4.38.0",
        "wandb==0.16.2",
        "webdataset>=0.2.86",
    ],
    python_requires=">=3.10",
)
