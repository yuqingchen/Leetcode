class Solution:
    def validIPAddress(self, IP: str) -> str:
        ips = IP.split('.')
        if len(ips) == 4 :
            for ip in ips :
                print(ip)
                print(ip.isdigit())
                if not ip.isdigit() or not 0 <= int(ip) < 256 or(ip[0] == '0' and len(ip) > 1) :
                    return 'Neither'
            return "IPv4"
        ips = IP.split(':')
        if len(ips) == 8 :
            for ip in ips :
                if len(ip) == 0 or not len(ip) <= 4 or not self.hex(ip) :
                    return "Neither"
            return "IPv6"
        return "Neither"
    
    def hex(self, ip) :
        hexdigit = set("0123456789abcdefABCDEF")
        for ch in ip :
            if not (ch in hexdigit) :
                return False
        return True