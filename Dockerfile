# Base CUDA image
FROM python:3.8

LABEL maintainer="OracleMemory2@gmail.com"
LABEL version="dev-20250331"
LABEL description="Docker image for GPT-SoVITS"

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    && rm -rf /var/lib/apt/lists/*

# CMake 다운로드 및 설치
WORKDIR /tmp
RUN wget https://github.com/Kitware/CMake/releases/download/v3.22.3/cmake-3.22.3.tar.gz && \
    tar -xvzf cmake-3.22.3.tar.gz && \
    cd cmake-3.22.3/ && \
    ./bootstrap && \
    make && \
    make install && \
    cd .. && \
    rm -rf cmake-3.22.3 cmake-3.22.3.tar.gz

# CMake 버전 확인
RUN cmake --version

# Install 3rd party apps
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTCpack_audio
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata ffmpeg libsox-dev parallel aria2 git git-lfs && \
    git lfs install && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt initially to leverage Docker cache

WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install --upgrade pip
RUN env CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install --no-cache-dir pyopenjtalk
RUN pip install --no-cache-dir -r requirements.txt


# # Define a build-time argument for image type
# ARG IMAGE_TYPE=full

# # Conditional logic based on the IMAGE_TYPE argument
# # Always copy the Docker directory, but only use it if IMAGE_TYPE is not "elite"
# COPY ./Docker /workspace/Docker 
# # elite 类型的镜像里面不包含额外的模型
# RUN if [ "$IMAGE_TYPE" != "elite" ]; then \
#         chmod +x /workspace/Docker/download.sh && \
#         /workspace/Docker/download.sh && \
#         python /workspace/Docker/download.py && \
#         python -m nltk.downloader averaged_perceptron_tagger cmudict; \
#     fi


# Copy the rest of the application
COPY . /workspace
EXPOSE 9880

CMD ["python", "api.py"]
