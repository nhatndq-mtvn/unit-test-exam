### Checklist

- [ ] Test should order status change to "exported" when export CSV succeeds while processing type A.
- [ ] Test should order status change to "export failed" when export CSV fails while processing type A.
- [ ] Test should order status change to "processed" when API data is 50 and order amount is less than 100 while processing type B.
- [ ] Test should order status change to "pending" when API data is less than 50 and order flag is true while processing type B.
- [ ] Test should order status change to "error" when API data is 50 and order flag is false while processing type B.
- [ ] Test should order status change to "API error" when API returns "fail" while processing type B.
- [ ] Test should order status change to "API failure" when API returns "error" while processing type B.
- [ ] Test should order status change to "completed" when order flag is true while processing type C.
- [ ] Test should order status change to "in progress" when order flag is false while processing type C.
- [ ] Test should order status change to "unknown type" when order flag is false while processing a different type.
- [ ] Test should return true and write CSV when processing order type A.
- [ ] Test should return true and not call API when processing order type A.
- [ ] Test should return true and not write CSV when processing order type B.
- [ ] Test should return true and call API when processing order type B.
- [ ] Test should return true and not write CSV when processing order type C.
- [ ] Test should return true and not call API when processing order type C.
- [ ] Test should return true and not write CSV when processing a different type.
- [ ] Test should return true and not call API when processing a different type.
- [ ] Test should return true and priority is high when processing order amount greater than 200.
- [ ] Test should return false when not processing an order.
- [ ] Test should return false when the function get orders by user encounters an error.
- [ ] Test should return false when the bulk update order status function encounters an error.