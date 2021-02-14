import setuptools
with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="trnames",
	version="0.1.0",
	author="Kaan Öztürk",
	author_email="mkaanozturk@gmail.com",
	description="Random Turkish name generator with realistic probabilities.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
    	install_requires=[],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
)
