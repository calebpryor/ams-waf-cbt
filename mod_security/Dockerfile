FROM pryor/aem-dispatcher-filter-testing:rockylinux8
USER root
RUN dnf -y --nogpgcheck install mod_security && \
    dnf clean all
RUN sed -i 's/DispatcherLogLevel trace/DispatcherLogLevel error/' /etc/httpd/conf.d/httpd-dispatcher.conf
RUN ln -sf /dev/stderr /var/log/httpd/modsec_audit.log && \
    ln -sf /dev/stderr /var/log/httpd/modsec_debug.log
ADD wide_open_farm.any /etc/httpd/conf.dispatcher.d/dispatcher.any
USER apache
EXPOSE 80
CMD /usr/local/bin/start.sh $DISP_VER