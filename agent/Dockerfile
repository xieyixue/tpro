FROM ubuntu:14.04
ADD sources.list /etc/apt/sources.list
ADD tasks.py /root/tasks.py
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install request
CMD ["python /root/tasks.py"]
