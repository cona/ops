FROM centos:centos7

RUN yum install -y wget tar gcc-c++ make mecab-devel && yum clean all
RUN wget http://packages.groonga.org/source/groonga/groonga-4.1.1.tar.gz
RUN tar zxvf groonga-4.1.1.tar.gz
RUN cd groonga-4.1.1 \
&& echo "CFLAGS = @CFLAGS@ --param max-gcse-memory=268435456" >> lib/Makefile.in \
&& ./configure \
&& make -j$(grep '^processor' /proc/cpuinfo | wc -l) \
&& make install

ADD services.sh /etc/services.sh
RUN chmod +x /etc/services.sh
ENTRYPOINT /etc/services.sh
