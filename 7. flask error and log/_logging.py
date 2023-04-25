import logging
# ERROR 이하의 것이 발생했을 때 log를 남기겠다.
# DEBUG > INFO > WARNING > ERROR > Critical

logging.basicConfig(filename='./test.log', level=logging.ERROR)

# 로그를 남길 부분에 다음과 같이 로그 레벨에 맞추어 출력해주면 해당 내용이 파일에 들어감
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


# test.log

# ERROR:root:error
# CRITICAL:root:critical