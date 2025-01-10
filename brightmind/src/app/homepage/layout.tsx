import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Home | BrightMind",
  description: "Welcome to BrightMind - Your Mental Health & Wellness Journey",
};

export default function HomeLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return children;
} 