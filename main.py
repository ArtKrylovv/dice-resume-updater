import schedule
from app.dice import dice_update
from utilities.config import get_data
from utilities.logger import get_logger


def main():
    """
    Schedules job using configurations from config.yaml file.
    """
    status = get_data()['autorun']['status']
    time = get_data()['autorun']['schedule']
    headless = get_data()['headless']
    max_attempts = get_data()['max_attempts']
    logger = get_logger()

    print('>>> starting new job')
    logger.debug(f'starting job with configuration: '
                 f'autorun: {status}, daily schedule at: {time}')
    if status:
        print(f'>>> run scheduled on {time} daily')
        schedule.every().day.at(time).do(dice_update, max_attempts, headless)
        while True:
            schedule.run_pending()
    else:
        dice_update(max_attempts, headless)


if __name__ == '__main__':
    main()
