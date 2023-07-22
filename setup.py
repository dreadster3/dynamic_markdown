import setuptools

basepath = "src"

setuptools.setup(
    name="dynamic_markdown",
    version="0.0.1",
    author="dreadster3",
    description="A CLI tool for rendering markdown files with variables",
    long_description=open("README.md").read(),
    package_dir={"": basepath},
    packages=setuptools.find_packages(where=basepath, exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "render_markdown = dynamic_markdown.main:main"
        ]
    },
    install_requires = [
        "PyYAML>=6.0.1",
    ]
)
