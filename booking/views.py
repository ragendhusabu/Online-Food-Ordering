
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


# Create your views here.

class About(View):
    def get(self,request):
        data = {
            "Website_Name": "Foodie Express",
            "Description": "An online food ordering platform.",
            "Email": "foodieexpress@gmail.com",
            "Contact": 9876543210,
            "Website": "https://www.foodieexpress.com",
            "Location": "Kochi, Kerala"
        }

        return JsonResponse(data)


class RestaurantView(View):
    def get(self,request):
        restaurants = [
            {
                "id": 1,
                "restaurant_name": "Spice Garden",
                "cuisine": "Indian",
                "location": "Kochi, Kerala",
                "contact": 9876543211,
                "rating": 4.5,
                "opening_time": "10:00 AM",
                "closing_time": "10:00 PM",
                "available": True
            },
            {
                "id": 2,
                "restaurant_name": "Pizza Corner",
                "cuisine": "Italian",
                "location": "Kozhikode, Kerala",
                "contact": 9876543212,
                "rating": 4.3,
                "opening_time": "11:00 AM",
                "closing_time": "11:00 PM",
                "available": True
            },
            {
                "id": 3,
                "restaurant_name": "Burger Hub",
                "cuisine": "Fast Food",
                "location": "Trivandrum, Kerala",
                "contact": 9876543213,
                "rating": 4.2,
                "opening_time": "12:00 PM",
                "closing_time": "11:00 PM",
                "available": True
            }
        ]

        return JsonResponse(restaurants,safe=False)


class MenuView(View):
    def get(self,request):
        menu = [
            {
                "id": 1,
                "restaurant_id": 1,
                "food_name": "Chicken Biryani",
                "category": "Main Course",
                "price": 180,
                "description": "Traditional Kerala-style chicken biryani.",
                "preparation_time": "25 minutes",
                "available": True
            },
            {
                "id": 2,
                "restaurant_id": 1,
                "food_name": "Paneer Butter Masala",
                "category": "Main Course",
                "price": 160,
                "description": "Paneer cooked in a creamy tomato-based gravy.",
                "preparation_time": "20 minutes",
                "available": True
            },
            {
                "id": 3,
                "restaurant_id": 2,
                "food_name": "Margherita Pizza",
                "category": "Pizza",
                "price": 250,
                "description": "Classic pizza with cheese and tomato sauce.",
                "preparation_time": "20 minutes",
                "available": True
            },
            {
                "id": 4,
                "restaurant_id": 3,
                "food_name": "Veg Burger",
                "category": "Burger",
                "price": 120,
                "description": "Fresh vegetable patty with lettuce and cheese.",
                "preparation_time": "15 minutes",
                "available": True
            },
            {
                "id": 5,
                "restaurant_id": 2,
                "food_name": "French Fries",
                "category": "Snacks",
                "price": 90,
                "description": "Crispy golden potato fries.",
                "preparation_time": "10 minutes",
                "available": True
            }
        ]

        return JsonResponse(menu,safe=False)


class CategoryView(View):
    def get(self,request):
        categories = [
            {
                "id": 1,
                "category_name": "Main Course",
                "description": "Rice, biryani and other main dishes.",
                "total_items": 25
            },
            {
                "id": 2,
                "category_name": "Pizza",
                "description": "Different varieties of pizzas.",
                "total_items": 15
            },
            {
                "id": 3,
                "category_name": "Burger",
                "description": "Vegetarian and non-vegetarian burgers.",
                "total_items": 12
            },
            {
                "id": 4,
                "category_name": "Snacks",
                "description": "Quick bites and evening snacks.",
                "total_items": 20
            },
            {
                "id": 5,
                "category_name": "Desserts",
                "description": "Cakes, ice creams and sweet dishes.",
                "total_items": 18
            }
        ]

        return JsonResponse(categories,safe=False)


class CustomerView(View):
    def get(self,request):
        customers = [
            {
                "id": 1,
                "customer_name": "Arun Kumar",
                "email": "arun@gmail.com",
                "phone": 9876543214,
                "location": "Kochi",
                "total_orders": 12
            },
            {
                "id": 2,
                "customer_name": "Meera Thomas",
                "email": "meera@gmail.com",
                "phone": 9876543215,
                "location": "Kozhikode",
                "total_orders": 8
            },
            {
                "id": 3,
                "customer_name": "Rahul Raj",
                "email": "rahul@gmail.com",
                "phone": 9876543216,
                "location": "Trivandrum",
                "total_orders": 15
            }
        ]

        return JsonResponse(customers,safe=False)


class OrderView(View):
    def get(self,request):
        orders = [
            {
                "id": 1,
                "customer_id": 1,
                "customer_name": "Arun Kumar",
                "restaurant_name": "Spice Garden",
                "food_name": "Chicken Biryani",
                "quantity": 2,
                "total_amount": 360,
                "order_date": "2026-11-01",
                "order_status": "Delivered"
            },
            {
                "id": 2,
                "customer_id": 2,
                "customer_name": "Meera Thomas",
                "restaurant_name": "Pizza Corner",
                "food_name": "Margherita Pizza",
                "quantity": 1,
                "total_amount": 250,
                "order_date": "2026-11-02",
                "order_status": "Preparing"
            },
            {
                "id": 3,
                "customer_id": 3,
                "customer_name": "Rahul Raj",
                "restaurant_name": "Burger Hub",
                "food_name": "Veg Burger",
                "quantity": 2,
                "total_amount": 240,
                "order_date": "2026-11-03",
                "order_status": "Out for Delivery"
            }
        ]

        return JsonResponse(orders,safe=False)


class DeliveryView(View):
    def get(self,request):
        deliveries = [
            {
                "id": 1,
                "order_id": 1,
                "delivery_person": "Sanjay Kumar",
                "phone": 9876543217,
                "delivery_address": "MG Road, Kochi",
                "delivery_status": "Delivered",
                "estimated_time": "30 minutes"
            },
            {
                "id": 2,
                "order_id": 2,
                "delivery_person": "Akhil Raj",
                "phone": 9876543218,
                "delivery_address": "Beach Road, Kozhikode",
                "delivery_status": "Preparing",
                "estimated_time": "40 minutes"
            },
            {
                "id": 3,
                "order_id": 3,
                "delivery_person": "Vishnu Das",
                "phone": 9876543219,
                "delivery_address": "Palayam, Trivandrum",
                "delivery_status": "Out for Delivery",
                "estimated_time": "20 minutes"
            }
        ]

        return JsonResponse(deliveries,safe=False)
