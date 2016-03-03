FROM ubuntu:14.04
ADD sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y ssh
RUN useradd admin  
RUN echo "admin:admin" | chpasswd  
RUN echo "admin   ALL=(ALL)       ALL" >> /etc/sudoers  
   
#RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
   
# Æ¶¯sshd·þÎ²¢Ç±©¶22¶˿Ú 
RUN mkdir /var/run/sshd  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
