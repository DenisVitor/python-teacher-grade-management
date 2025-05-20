def main():
    grades = []
    while True:
        grade = input("Digite a nota (0-10) ou 'fim' para encerrar: ").strip().lower()
        if grade == "fim":
            break
        try:
            note = float(grade)
        except ValueError:
            print("Entrada inválida. Digite um número entre 0 e 10, ou 'fim'.\n")
            continue
        if 0 <= note <= 10:
            grades.append(note)
        else:
            print("Nota inválida. Deve ser entre 0 e 10.\n")
    if grades:
        avg = sum(grades) / len(grades)
        print(f"\nMédia da turma ({len(grades)} notas): {avg:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


if __name__ == "__main__":
    main()
