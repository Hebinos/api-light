FROM python:3.6

ARG pj_dir=/pj/

ADD src/requirements.txt $pj_dir
ADD src/config.cfg $pj_dir

WORKDIR $pj_dir

RUN pip install -r requirements.txt
RUN export FLASK_APP=api-light
RUN export FLASK_DEBUG=true
