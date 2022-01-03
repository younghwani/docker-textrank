# basing on ubuntu OS
FROM ubuntu:latest
LABEL maintainer="Younghwani <younghwankim624@gmail.com>"

# apt init
ENV LANG=C.UTF-8
ENV TZ=Asia/Seoul
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y --no-install-recommends tzdata g++ git curl

# install Java jdk and jre
RUN apt-get install -y openjdk-8-jdk
ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

# install Python and pip
RUN apt-get install -y python3-pip python3-dev
RUN cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    ln -s /usr/bin/pip3 pip && \
    pip3 install --upgrade pip

# apt clean
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# timezone
RUN ln -sf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# copy resource
COPY . .

# install python package
RUN pip install -r requirements.txt

#Expose port to 5000
EXPOSE 5000

CMD python ./app.py