# Base image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Install system-level build tools
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*


# set working dir
WORKDIR /

# copy essential files
COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY README.md README.md
COPY src/ src/
COPY data/ data/

# Install py dependencies
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv uv sync


# run train when container starts
ENTRYPOINT ["uv", "run", "src/cookie_cutter_demo/train.py"]
