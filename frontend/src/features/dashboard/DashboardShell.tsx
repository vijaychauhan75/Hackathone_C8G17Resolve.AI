"use client";

import { Upload, BookOpen, Settings, HelpCircle } from "lucide-react";
import { Button } from "@/components/ui/button";

const navItems = [
  { icon: Upload, label: "Upload Logs", href: "/upload" },
  { icon: BookOpen, label: "Knowledge Base", href: "/knowledge" },
  { icon: Settings, label: "RAG Configuration", href: "/rag" },
  { icon: HelpCircle, label: "Help", href: "/help" },
];

export default function DashboardShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="flex h-screen">
      <aside className="w-64 border-r bg-slate-50">
        <div className="p-4">
          <h2 className="text-lg font-semibold mb-4">Resolve.AI</h2>
          <nav className="space-y-1">
            {navItems.map((item) => (
              <Button
                key={item.href}
                variant="ghost"
                className="w-full justify-start"
                asChild
              >
                <a href={item.href}>
                  <item.icon className="mr-2 h-4 w-4" />
                  {item.label}
                </a>
              </Button>
            ))}
          </nav>
        </div>
      </aside>
      <div className="flex-1 overflow-auto">{children}</div>
    </div>
  );
}