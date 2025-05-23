import pandas as pd

def update_club_members():
    try:
        # Load files
        club_df = pd.read_excel("club_members.xlsx")
        titan_df = pd.read_csv("titanlink_roster.csv")

        # Rename TitanLink columns to match club file
        titan_df.rename(columns={
            "Full Name": "Name",
            "Email Address": "Email",
            "Dues Paid": "Paid"
        }, inplace=True)

        # Merge and remove duplicates based on Email
        merged_df = pd.concat([club_df, titan_df])
        merged_df = merged_df.drop_duplicates(subset="Email", keep="last")

        # Save the updated Excel file
        merged_df.to_excel("club_members.xlsx", index=False)
        print("✅ club_members.xlsx updated successfully!")

    except Exception as e:
        print(f"❌ Error updating members: {e}")

if __name__ == "__main__":
    update_club_members()

