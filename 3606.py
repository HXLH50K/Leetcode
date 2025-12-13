from typing import List


class Coupon:
    def __init__(self, code: str, businessLine: str, isActive: bool):
        self.code = code
        self.businessLine = businessLine
        self.isActive = isActive


class Solution:
    def isValidCoupon(self, coupon: Coupon) -> bool:
        if not coupon.isActive:
            return False

        if coupon.businessLine not in {
            "electronics",
            "grocery",
            "pharmacy",
            "restaurant",
        }:
            return False

        return bool(coupon.code) and all(c.isalnum() or c == "_" for c in coupon.code)

    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        n = len(code)
        coupons = [Coupon(code[i], businessLine[i], isActive[i]) for i in range(n)]
        valid_coupons = []
        for coupon in coupons:
            if self.isValidCoupon(coupon):
                valid_coupons.append(coupon)
        valid_coupons.sort(key=lambda x: (x.businessLine, x.code))
        return [coupon.code for coupon in valid_coupons]
