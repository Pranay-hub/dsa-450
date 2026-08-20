import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "DSA 450 - Coding Interview Problems",
  description: "450+ Data Structures & Algorithms problems with optimized solutions, explanations, and visualizations",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}>
      <body className="min-h-full flex flex-col" suppressHydrationWarning>
        <header className="sticky top-0 z-50 border-b border-border bg-surface/80 backdrop-blur-md">
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div className="flex h-14 items-center justify-between">
              <Link href="/" className="flex items-center gap-2 font-bold text-lg">
                <span className="text-primary">DSA</span>
                <span className="text-foreground">450</span>
              </Link>
              <nav className="flex items-center gap-4 text-sm text-zinc-400">
                <Link href="/" className="hover:text-foreground transition-colors">Problems</Link>
                <a href="https://github.com/loveBabbar/DSA450" target="_blank" rel="noopener" className="hover:text-foreground transition-colors">GitHub</a>
              </nav>
            </div>
          </div>
        </header>
        <main className="flex-1">{children}</main>
        <footer className="border-t border-border py-6 text-center text-sm text-zinc-500">
          DSA 450 &mdash; Curated by Love Babbar
        </footer>
      </body>
    </html>
  );
}
