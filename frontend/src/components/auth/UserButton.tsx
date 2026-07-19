"use client"

import { useUser, SignInButton, SignOutButton } from "@clerk/nextjs";
import { Button } from "@/components/ui/button";

export default function UserButton() {
  const { isSignedIn, user } = useUser();

  if (!isSignedIn) {
    return (
      <SignInButton mode="modal">
        <Button size="sm">Sign in</Button>
      </SignInButton>
    );
  }

  return (
    <SignOutButton>
      <Button variant="outline" size="sm">
        Sign out ({user.username || user.primaryEmailAddress?.emailAddress})
      </Button>
    </SignOutButton>
  );
}