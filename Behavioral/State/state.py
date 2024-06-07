from abc import ABC, abstractmethod


class ICheckoutState(ABC):
    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def review_cart(self):
        pass

    @abstractmethod
    def enter_shipping_info(self, info):
        pass

    @abstractmethod
    def process_payment(self):
        pass


class EmptyCartState(ICheckoutState):

    def add_item(self, item: str) -> 'ItemAddedState':
        print("Item added to the cart.")
        return ItemAddedState()

    def review_cart(self):
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info: str):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


class ItemAddedState(ICheckoutState):

    def add_item(self, item: str):
        print("Item added to the cart.")

    def review_cart(self) -> 'CartReviewedState':
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info: str):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(ICheckoutState):

    def add_item(self, item: str):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info: str) -> 'ShippingInfoEnteredState':
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(ICheckoutState):

    def __init__(self, info: str):
        self.info = info

    def add_item(self, item: str):
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info: str):
        print("Shipping information already entered.")

    def process_payment(self):
        print("Processing payment with the entered shipping info.")


class CheckoutContext:

    def __init__(self):
        self.__current_state = EmptyCartState()

    def add_item(self, item: str):
        self.__current_state = self.__current_state.add_item(item)

    def review_cart(self):
        self.__current_state.review_cart()

    def enter_shipping_info(self, info: str):
        self.__current_state.enter_shipping_info(info)

    def process_payment(self):
        self.__current_state.process_payment()


# Step 4: Example of Usage
if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("Test")
    cart.review_cart()
    cart.enter_shipping_info("Test info")
    cart.process_payment()
