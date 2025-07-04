from prompt_engine import PromptEngine

def main():
    print("Bem-vindo à Alice IA! Digite 'sair' para encerrar.")
    engine = PromptEngine()

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Alice: Até mais!")
            break

        response = engine.generate_response(user_input)
        print(f"Alice: {response}")

if __name__ == "__main__":
    main()