from utils import mani, gen_bro
from time import sleep
from selenium.common.exceptions import NoSuchElementException

url = 'https://portal.pku.edu.cn/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

account = {
    'id': 'xxx',
    'pass': 'xxx'
}


def main(dvr_root=r'./chromedriver'):
    bro = gen_bro(root=dvr_root)
    bro.get(url)

    # Loggin portal
    try:
        bro.find_element_by_xpath('//*[@id="ng-app"]/div[1]/header/section/section[1]/section[1]/ul[1]/li/a').click()
    except NoSuchElementException: # The page's been auto relocated
        sleep(2)

    id_input = bro.find_element_by_id('user_name')
    id_input.send_keys(account['id'])
    pass_input = bro.find_element_by_id('password')
    pass_input.send_keys(account['pass'])
    bro.find_element_by_id('logon_button').click()
    sleep(3)

    # try:
    #     btn = bro.find_element_by_xpath('//*[@id="bizTip"]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a')
    #     print('Here')
    #     btn.click()
    #     print('click')
    # except NoSuchElementException:
    #     pass

    bro.refresh()
    sleep(3)
    bro.find_element_by_id('all').click()
    bro.find_element_by_id('fav_epidemic').click()
    sleep(10)
    mani(bro)


if __name__ == '__main__':
    main()