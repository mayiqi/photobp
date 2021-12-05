.. photobp documentation master file, created by
   sphinx-quickstart on Sun Dec  5 16:00:14 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

**Lab 2**: Use blueprints to architect a web application
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**小组成员**

201932110105沈音棋

201932110104马奕琪

201932110106孙仪杰

201932110107田西芷

**项目GitHub地址**: `photobp`_.

.. _EnglishPal: https://github.com/ChiefEye-official/Test/

**项目Read the Doc地址**: `Read the Doc`_.

.. _Read The Doc: https://readthedocs.org/projects/testenglishpal/

Abstract
=================================================

Use blueprints to organize a web application.

Introduction
=================================================

Photo String is a web album for storing photos, allowing us to upload an image and add a description to that image.

This experiment adds upload_bp, show_bp, search_bp, and api_bp to the project through blueprints.

The upload bp blueprint allows uploading a new photo. The associated route is /upload.

The show bp blueprint allows displaying all photos and their descriptions in chronological order. The associated route is /show.

The search bp blueprint allows filtering photos according to their descriptions. The associated route is /search/query-string. Only the photos whose descriptions match query-string will be returned as the search result.

The api bp blueprint allows us to get all photo information in JSON format from command-line. HTTPie is a useful API testing tool. The associated route is /api/json. The returned json string must contain photo ID, date of upload, photo size (in KB) and photo description for each photo.

Methods and materials
=================================================

①blueprint: Blueprint是一个存储视图方法的容器，这些操作在这个Blueprint 被注册到一个应用之后就可以被调用，Flask 可以通过Blueprint来组织URL以及处理请求。

②HTTPie:HTTPie 是一个 HTTP 的命令行客户端，目标是让 CLI 和 web 服务之间的交互尽可能的人性化。这个工具提供了简洁的 http 命令，允许通过自然的语法发送任意 HTTP 请求数据，展示色彩化的输出。HTTPie 可用于与 HTTP 服务器做测试、调试和常规交互。

Results
=================================================



References
=================================================

