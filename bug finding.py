car_problems = ["car won't start",
                "engine over heating"
    ,"flat tire/low tire pressure"
    ,"car pulls to one side while driving"
    ,"brakes feel spongy/noisy"
    ,"strange noises from engine"
    ,"battery keeps dying"
                ]
solutions = {
    1: "Check the battery, jump-start the car, or check the starter motor.",
   2: "Stop driving, check coolant level, refill if low, or check radiator fan.",
   3: "Use a spare tire, repair kit, or inflate the tire and go to a repair shop.",
    4: "Check tire pressure or get a wheel alignment.",
   5: "Replace brake pads or check brake fluid.",
    6: "Replace the battery or check if the alternator is charging properly.",
   7: "Check oil level, tighten belts, or replace spark plugs."
}

print("what problem your car have?: ")
for i,problem in enumerate(car_problems, start=1):
    print(f"{i}. {problem}")
user_choice = int(input("what is your problem: "))
if  user_choice in solutions:
    selected_problem = car_problems[user_choice - 1]
    print(f"\n✅ Problem: {user_choice}")
    print(f"🔧 Fix: {solutions[user_choice]}")
else:
        print("\n❌ Invalid choice. Please select a number from the list.")

