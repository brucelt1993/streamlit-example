import requests
import re
from bs4 import BeautifulSoup
import streamlit as st

def extract_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    images = []
    for img in soup.find_all("img"):
        src = img.attrs.get("src")
        if src:
            src = re.sub("^//", "https://", src)
            images.append(src)
    return images

def main():
    st.title("图片提取器")
    url = st.text_input("输入url:")
    if st.button("提取链接"):
        images = extract_images(url)
        if not images:
            st.error("当前页面无图片")
        else:
            st.success("发现 {} 张图片.".format(len(images)))
            for i, image in enumerate(images):
                st.write("Image {}:".format(i + 1))
                st.write("URL: {}".format(image))
                st.write("Download:")
                st.markdown("[Download]({})".format(image))

if __name__ == "__main__":
    main()
