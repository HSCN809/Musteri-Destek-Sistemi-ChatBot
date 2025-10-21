"""
Müşteri Profil Memory Sistemi
"""
from typing import Dict, List
import datetime


class CustomerProfileMemory:
    """Müşteri etkileşimlerini ve tercihlerini saklar"""
    
    def __init__(self):
        self.profiles = {}
    
    def update_interaction(self, customer_id: str, category: str, 
                          sentiment: str = "nötr"):
        """
        Müşteri etkileşimini güncelle
        
        Args:
            customer_id: Müşteri ID
            category: Etkileşim kategorisi
            sentiment: Duygu durumu
        """
        if customer_id not in self.profiles:
            self.profiles[customer_id] = {
                "total_interactions": 0,
                "categories": {},
                "sentiments": {},
                "last_interaction": None,
                "preferences": {}
            }
        
        profile = self.profiles[customer_id]
        profile["total_interactions"] += 1
        profile["last_interaction"] = datetime.datetime.now().isoformat()
        
        # Kategori istatistikleri
        if category not in profile["categories"]:
            profile["categories"][category] = 0
        profile["categories"][category] += 1
        
        # Duygu istatistikleri
        if sentiment not in profile["sentiments"]:
            profile["sentiments"][sentiment] = 0
        profile["sentiments"][sentiment] += 1
    
    def get_statistics(self, customer_id: str) -> Dict:
        """
        Müşteri istatistiklerini getir
        
        Args:
            customer_id: Müşteri ID
            
        Returns:
            İstatistikler dictionary
        """
        if customer_id not in self.profiles:
            return {
                "total_interactions": 0,
                "message": "Müşteri bulunamadı"
            }
        
        profile = self.profiles[customer_id]
        
        # En çok kullanılan kategori
        favorite_category = max(
            profile["categories"].items(),
            key=lambda x: x[1],
            default=("yok", 0)
        )[0]
        
        # En yaygın duygu
        common_sentiment = max(
            profile["sentiments"].items(), 
            key=lambda x: x[1],
            default=("nötr", 0)
        )[0]
        
        return {
            "total_interactions": profile["total_interactions"],
            "favorite_category": favorite_category,
            "common_sentiment": common_sentiment,
            "categories": profile["categories"],
            "sentiments": profile["sentiments"],
            "last_interaction": profile["last_interaction"]
        }
    
    def get_preferences(self, customer_id: str) -> Dict:
        """
        Müşteri tercihlerini getir
        
        Args:
            customer_id: Müşteri ID
            
        Returns:
            Tercihler dictionary
        """
        if customer_id not in self.profiles:
            return {}
        
        return self.profiles[customer_id].get("preferences", {})
    
    def update_preferences(self, customer_id: str, preferences: Dict):
        """
        Müşteri tercihlerini güncelle
        
        Args:
            customer_id: Müşteri ID
            preferences: Yeni tercihler
        """
        if customer_id not in self.profiles:
            self.profiles[customer_id] = {
                "total_interactions": 0,
                "categories": {},
                "sentiments": {},
                "last_interaction": None,
                "preferences": {}
            }
        
        self.profiles[customer_id]["preferences"].update(preferences)
    
    def clear_customer_data(self, customer_id: str):
        """Müşteri verilerini temizle"""
        if customer_id in self.profiles:
            del self.profiles[customer_id]
    
    def get_all_customers(self) -> List[str]:
        """Tüm müşteri ID'lerini getir"""
        return list(self.profiles.keys())