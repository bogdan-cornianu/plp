__author__ = 'bogdan.cornianu'
from Logger import Logger


def dummy_exec():
    pass


def test_log():
    logger = Logger("../../res/logger.conf")
    logger.error("ERROOORRRROORORO!!!")
    logger.critical("Now you should be worried.")
    logger.info("JUST INFO, DON'T WORRY.")

dummy_exec()
test_log()