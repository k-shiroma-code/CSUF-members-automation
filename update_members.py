import pandas as pd

def update_club_members():
    try:

        club_df = pd.read_excel("club_members.xlsx")
        titan_df = pd.read_csv("titanlink_roster.csv")

        titan_df.rename(columns={
            "Full Name": "Name",
            "Email Address": "Email",
            "Dues Paid": "Paid"
        }, inplace=True)

        merged_df = pd.concat([club_df, titan_df])
        merged_df = merged_df.drop_duplicates(subset="Email", keep="last")

        merged_df.to_excel("club_members.xlsx", index=False)
        print("✅ club_members.xlsx updated successfully!")

    except Exception as e:
        print(f"❌ Error updating members: {e}")

if __name__ == "__main__":
    update_club_members()

