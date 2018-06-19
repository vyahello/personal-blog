FROM vyahello/yfox-base:0.1.0
LABEL metadata="Main image for YFox blog" \
      version=1.0.0 \
      maintainer="Volodymyr Yahello <vjagello93@gmail.com>"
WORKDIR /blog
COPY server server
COPY requirements.txt yfox.py ./
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt
ENTRYPOINT python yfox.py
