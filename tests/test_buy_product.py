@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestBuyProduct:
    def test_buy_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.checkout()