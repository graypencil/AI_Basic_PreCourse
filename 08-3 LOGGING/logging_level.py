import logging


# 설정이 되어 있지 않는 경우는 warning 단계부터 알림
if __name__ == '__main__':
    logger = logging.getLogger("main")
    logging.basicConfig(level=logging.DEBUG)  # DEBUG 부터 alarm을 설정하라! (setting 변경)
    logger.setLevel(logging.ERROR)  # Error level 부터 알려라
    

    # mylog 파일에 저장하라
    steam_handler = logging.FileHandler(
         "my.log", mode = "a", encoding = "UTF8")
    logger.addHandler(steam_handler)

    
    logger.debug("틀렸어!")
    logger.info("확인행!!")
    logger.warning("조심해!!")
    logger.error("에러났어!!")
    logger.critical("망했다!!")


