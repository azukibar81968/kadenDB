FROM postgres:latest

WORKDIR /app

RUN apt-get update
RUN apt-get upgrade -y

ENV TZ=Asia/Tokyo 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get install -y python3-pip


RUN apt install -y git

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install libpq-dev -y
RUN pip install psycopg2

RUN pip install flask
ENV PYTHONPATH="./usr/lib/python3.8/site-packages/:$PYTHONPATH"


#RUN python3 endpoint.py data/sample/bin/  --path checkpoints/japanese-dialog-transformer-1.6B.pt  --beam 80  --min-len 10  --source-lang src  --target-lang dst  --tokenizer space  --bpe sentencepiece  --sentencepiece-model data/dicts/sp_oall_32k.model  --no-repeat-ngram-size 3  --nbest 80  --sampling  --sampling-topp 0.9  --temperature 1.0  --show-nbest 5




# sudo docker build -t fairseq_transformer:sweethome ./
# sudo docker run --rm -it -p 8080:80 --gpus all fairseq_transformer:sweethome /bin/bash