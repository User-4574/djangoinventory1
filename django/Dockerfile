FROM python:latest
# Section 2- Python Interpreter Flags
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
#Pull variables from runtime.
ARG APP_USER
ENV APP_USER=$APP_USER
ARG APP_USER_ID
ENV APP_USER_ID=$APP_USER_ID
ENV PATH=/wheels/bin:/scripts:${PATH}
ENV PYTHONPATH=${PYTHONPATH}:/wheels
RUN useradd -U ${APP_USER} -u ${APP_USER_ID} \
    && mkdir /scripts \
    && mkdir /wheels \
    && chown ${APP_USER} /wheels \
    && chown -R ${APP_USER}:${APP_USER} /scripts \
    && echo "SystemV/CST6CDT" /etc/timezone \
    && apt-get update \
    && apt-get install -y --no-install-recommends procps nginx \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
COPY --chown=${APP_USER}:${APP_USER} scripts/* /scripts/
COPY --chown=${APP_USER}:${APP_USER} scripts/* /scripts/
#USER ${APP_USER}:${APP_USER}
RUN pip install --target=/wheels --no-cache-dir -r /scripts/requirements.txt
ENTRYPOINT [ "/scripts/entrypoint.sh" ]
#Test
#CMD [ "/scripts/start.sh", "server" ]
#django_filters
