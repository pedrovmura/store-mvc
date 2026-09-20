from model.inventory import StockItem

class InventoryView:
    def show(self, item: StockItem) -> None:
        print(item)

    def show_list(self, items: list[StockItem]) -> None:
        for item in items:
            print(item)

    def show_alert(self, item: StockItem) -> None:
        print(f"Warning! Low Stock on {item}")

    def prompt_data(self) -> dict:
        sku = input("SKU: ")
        
        while True:
            try:
                quantity = int(input("Quantity: "))
                break
            except ValueError:
                print('Dado inválido, digite um valor inteiro.\n')
        
        while True:
            try:
                min_stock = int(input("Min stock: "))
                break
            except ValueError:
                print('Dado inválido, digite um valor inteiro.\n')
        
        shelf = input("Shelf code: ")
        
        return {
            "sku": sku,
            "quantity": quantity,
            "min_stock": min_stock,
            "shelf": shelf,
        }