def zoo_agent(query):
    query = query.lower()

    if "polar bear" in query:
        return "Polar bears mainly eat seals and are apex predators in the Arctic."
    elif "lion" in query:
        return "Lions are carnivorous animals known as the king of the jungle."
    elif "elephant" in query:
        return "Elephants are herbivores and the largest land animals."
    else:
        return "I can help with animal-related questions like lions, elephants, and polar bears."


print("AI Zoo Agent Ready! Type 'exit' to quit.\n")

while True:
    user_input = input("Ask: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    response = zoo_agent(user_input)
    print("AI Agent:", response)
