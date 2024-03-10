{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 50,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L24baruqdgRi",
        "outputId": "f5dc4536-b5ff-4c16-cf54-39e418d95c5d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "numero de linhas: 10\n",
            "numero de colunas: 10\n",
            "[378, 23, 719, 520, 870, 770, 767, 984, 991, 785]\n",
            "[91, 796, 239, 512, 889, 53, 65, 758, 45, 595]\n",
            "[998, 686, 285, 754, 19, 541, 412, 641, 203, 724]\n",
            "[313, 52, 504, 204, 106, 790, 338, 670, 5, 614]\n",
            "[528, 760, 482, 446, 883, 403, 853, 724, 110, 355]\n",
            "[64, 281, 48, 747, 403, 73, 988, 781, 154, 186]\n",
            "[203, 535, 331, 636, 51, 899, 740, 337, 599, 892]\n",
            "[343, 288, 763, 7, 682, 896, 946, 134, 733, 877]\n",
            "[857, 500, 435, 763, 348, 257, 298, 836, 580, 901]\n",
            "[98, 557, 283, 451, 552, 785, 147, 583, 453, 49]\n"
          ]
        }
      ],
      "source": [
        "#exerc_1\n",
        "import random\n",
        "\n",
        "linhas = int(input('numero de linhas: '))\n",
        "colunas = int(input('numero de colunas: '))\n",
        "\n",
        "def funcao(linhas, colunas):\n",
        "  matriz = []\n",
        "\n",
        "  for i in range(linhas):\n",
        "    linha = [0] * colunas\n",
        "\n",
        "    for j in range(len(linha)):\n",
        "      linha[j] = random.randint(0, 999)\n",
        "      \n",
        "    matriz.append(linha)\n",
        "    print(matriz[i])\n",
        "  \n",
        " \n",
        "\n",
        "funcao(linhas, colunas);\n",
        "\n"
      ]
    }
  ]
}