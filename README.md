# python_utility_scripts
  ## Simple Http Proxy { http_proxy.py + http_proxy.Dockerfile }
     Just a simple python http proxy so we can see what is happening or just proxy a get/post(will add other methods later.
     docker build command: docker build -t simple_http_proxy:0.1 . -f http_proxy.Dockerfile
     docker run command: docker run -p 8081:8081 -e PROXY_HOST='https://httpbin.org' -e LOGGING='TRUE' --name shp simple_http_proxy:0.1

     
