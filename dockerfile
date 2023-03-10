FROM jupyter/datascience-notebook:b418b67c225b

RUN curl "https://moji.or.jp/wp-content/ipafont/IPAexfont/ipaexg00401.zip" > font.zip
RUN unzip font.zip
RUN cp ipaexg00401/ipaexg.ttf /opt/conda/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/ipaexg.ttf
RUN echo "font.family : IPAexGothic" >>  /opt/conda/lib/python3.9/site-packages/matplotlib/mpl-data/matplotlibrc
RUN rm -r font.zip ipaexg00401/
RUN rm -r ./.cache

RUN pip install --upgrade pip
RUN pip install folium==0.12.1.post1