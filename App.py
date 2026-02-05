import streamlit as st
import pandas as pd
import os

ARQUIVO_DADOS = 'dados.csv'


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return pd.DataFrame(columns=['ID', 'Nome', 'Cargo', 'Salário'])
    return pd.read_csv(ARQUIVO_DADOS)


def salvar_dados(df):
    df.to_csv(ARQUIVO_DADOS, index=False)


st.title("Sistema CRUD com Streamlit e Pandas")
df = carregar_dados()

menu = st.sidebar.selectbox(
    "Menu", ["Ler (Read)", "Criar (Create)", "Atualizar (Update)", "Deletar (Delete)"])

if menu == "Ler (Read)":
    st.subheader("Visualizar Dados")
    if df.empty:
        st.info("Nenhum dado encontrado.")
    else:
        st.dataframe(df, use_container_width=True)

elif menu == "Criar (Create)":
    st.subheader("Adicionar Novo Registro")

    col1, col2 = st.columns(2)
    with col1:
        novo_id = st.number_input("ID", min_value=1, step=2)
        nome = st.text_input("Nome")
    with col2:
        cargo = st.text_input("Cargo")
        salario = st.number_input("Salário", min_value=0.0, format="%.2f")

    if st.button("Salvar"):
        if novo_id in df["ID"].values:
            st.error(f"O ID {novo_id} já existe.")
        else:
            novo_dado = pd.DataFrame(
                [{"ID": novo_id, "Nome": nome, "Cargo": cargo, "Salário": salario}])
            df = pd.concat([df, novo_dado], ignore_index=True)
            salvar_dados(df)
            st.success("Registro adicionado com sucesso!")

elif menu == "Atualizar (Update)":
    st.subheader("Editar Registro Existente")

    if df.empty:
        st.warning("Não há dados para atualizar.")
    else:
        id_para_editar = st.selectbox(
            "Selecione o ID para editar", df["ID"].unique())

        dados_atuais = df[df["ID"] == id_para_editar].iloc[0]

        novo_nome = st.text_input("Novo Nome", value=dados_atuais["Nome"])
        novo_cargo = st.text_input("Novo Cargo", value=dados_atuais["Cargo"])
        novo_salario = st.number_input("Novo Salário", value=float(
            dados_atuais["Salário"]), format="%.2f")

        if st.button("Atualizar"):
            df.loc[df["ID"] == id_para_editar, ["Nome", "Cargo", "Salário"]] = [
                novo_nome, novo_cargo, novo_salario]
            salvar_dados(df)
            st.success(f"ID {id_para_editar} atualizado com sucesso!")

elif menu == "Deletar (Delete)":
    st.subheader("Remover Registro")

    if df.empty:
        st.warning("Não há dados para deletar.")
    else:
        id_para_deletar = st.selectbox(
            "Selecione o ID para deletar", df["ID"].unique())

        if st.button(f"Deletar ID {id_para_deletar}"):
            df = df[df["ID"] != id_para_deletar]
            salvar_dados(df)
            st.success("Registro deletado!")
            st.rerun()
