from selenium.webdriver.common.by import By


def test_mobile_green(element): #---Проверил все условия (зеленый,желтый экран. кнопку случайное число. число)
        element(By.XPATH, '//android.widget.Button[@content-desc="зеленый"]').click()
        assert element(By.XPATH, '//(//android.view.View[@content-desc="Зеленый экран"])[1]')
        element(By.XPATH, '//android.widget.Button').click()
        assert element(By.XPATH, '//android.view.View[@content-desc="Стартовый экран"]')
        element(By.XPATH, '//android.widget.Button[@content-desc="желтый"]').click()
        assert element(By.XPATH, '//android.view.View[@content-desc="Желтый экран"]')
        element(By.XPATH, '//android.widget.Button[@content-desc="Случайное число"]').click()
        assert element(By.XPATH, '//android.view.View[@content-desc]')
        element(By.XPATH, '//android.widget.Button').click()
        assert element(By.XPATH, '//android.view.View[@content-desc="Стартовый экран"]')