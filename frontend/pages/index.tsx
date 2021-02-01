import React from "react";
import { NextPageContext } from "next";
import { User } from "../types";
import { doApiRequest } from "../utils/fetch";
import Accounts from "../components/Accounts/Accounts";

interface AccountPageProps {
    user: User;
}

// TODO: auth-gate that just does a redirect to platform's login route
const AccountPage = ({ user }: AccountPageProps) => <Accounts user={user} />;

AccountPage.getInitialProps = async (
    context: NextPageContext
): Promise<AccountPageProps> => {
    const headers = {
        headers: context.req
            ? { cookie: context.req.headers.cookie }
            : undefined,
    };
    const user: User = await doApiRequest(
        "/accounts/me/",
        headers
    ).then((res) => res.json());
    return { user };
};

export default AccountPage;