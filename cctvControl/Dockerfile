FROM python:3.8.10
COPY . /app
WORKDIR /app
#RUN apt-get update -y && pip install --upgrade pip && pip install opencv-python mesa -y # && apt-get install libgl1-mesa-glx install x11-apps xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic xorg openbox -y
RUN python -m pip install opencv-python
RUN python test.py